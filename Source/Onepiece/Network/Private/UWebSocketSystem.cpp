// Copyright (c) 2025 Doppleddiggong. All rights reserved. Unauthorized copying, modification, or distribution of this file, via any medium is strictly prohibited. Proprietary and confidential.

/**
 * @file UWebSocketSystem.cpp
 * @brief UWebSocketSystem의 동작을 구현합니다.
 */

#include "UWebSocketSystem.h"
#include "NetworkData.h"
#include "WebSocketsModule.h"
#include "NetworkLog.h"
#include "Misc/Base64.h"

// --- Subsystem Lifecycle ---

void UWebSocketSystem::Initialize(FSubsystemCollectionBase& Collection)
{
	Super::Initialize(Collection);
	bIsExpectingAudio = false;
}

void UWebSocketSystem::Deinitialize()
{
	if (WebSocket.IsValid())
	{
		// Unbind all delegates
		WebSocket->OnConnected().RemoveAll(this);
		WebSocket->OnConnectionError().RemoveAll(this);
		WebSocket->OnClosed().RemoveAll(this);
		WebSocket->OnMessage().RemoveAll(this);
		WebSocket->OnBinaryMessage().RemoveAll(this);

		if (WebSocket->IsConnected())
		{
			WebSocket->Close();
		}
	}
	Super::Deinitialize();
}

// --- Client Actions ---

void UWebSocketSystem::Connect()
{
	if (IsConnected())
	{
		LogNetwork(TEXT("Already connected."));
		return;
	}

	const FString Url = NetworkConfig::GetSocketURL();
	if (Url.IsEmpty())
	{
		LogNetwork(TEXT("WebSocket URL is empty. Please check your configuration in DefaultMyNetwork.ini."));
		return;
	}

	LogNetwork(FString::Printf(TEXT("Connecting to %s"), *Url));

	FWebSocketsModule& WebSocketModule = FModuleManager::LoadModuleChecked<FWebSocketsModule>(TEXT("WebSockets"));
	WebSocket = WebSocketModule.CreateWebSocket(Url, TEXT("ws"));

	// Bind native delegates
	WebSocket->OnConnected().AddUObject(this, &UWebSocketSystem::OnConnected_Native);
	WebSocket->OnConnectionError().AddUObject(this, &UWebSocketSystem::OnConnectionError_Native);
	WebSocket->OnClosed().AddUObject(this, &UWebSocketSystem::OnClosed_Native);
	WebSocket->OnMessage().AddUObject(this, &UWebSocketSystem::OnMessage_Native);
	WebSocket->OnBinaryMessage().AddUObject(this, &UWebSocketSystem::OnBinaryMessage_Native);

	WebSocket->Connect();
}

void UWebSocketSystem::Disconnect()
{
	if (WebSocket.IsValid() && WebSocket->IsConnected())
	{
		LogNetwork(TEXT("Disconnecting..."));
		WebSocket->Close();
	}
}

bool UWebSocketSystem::IsConnected() const
{
	return WebSocket.IsValid() && WebSocket->IsConnected();
}

void UWebSocketSystem::SendPing()
{
	if (!IsConnected())
	{
		LogNetwork(TEXT("Cannot send ping. Not connected."));
		return;
	}
    
	LogNetwork(TEXT("Sending Ping"));
	WebSocket->Send(TEXT("{\"type\":\"ping\"}"));
}

// --- Native WebSocket Callbacks ---

void UWebSocketSystem::OnConnected_Native()
{
	LogNetwork(TEXT("Connection successful."));
	bIsExpectingAudio = false;
	// OnConnected.Broadcast();
}

void UWebSocketSystem::OnConnectionError_Native(const FString& InErrorMessage)
{
	LogNetwork(FString::Printf(TEXT("Connection failed: %s"), *InErrorMessage));
	// OnConnectionError.Broadcast(InErrorMessage);
}

void UWebSocketSystem::OnClosed_Native(int32 StatusCode, const FString& Reason, bool bWasClean)
{
	LogNetwork(FString::Printf(TEXT("Connection closed. Code: %d, Reason: %s, Clean: %s"), StatusCode, *Reason, bWasClean ? TEXT("true") : TEXT("false")));
	bIsExpectingAudio = false;
	// OnClosed.Broadcast(StatusCode, Reason, bWasClean);
}

void UWebSocketSystem::OnMessage_Native(const FString& InMessage)
{
	TSharedPtr<FJsonObject> JsonObject;
	TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(InMessage);

	if (!FJsonSerializer::Deserialize(Reader, JsonObject) || !JsonObject.IsValid())
	{
		LogNetwork(FString::Printf(TEXT("Failed to parse incoming JSON message: %s"), *InMessage));
		return;
	}

	FString MessageType;
	if (!JsonObject->TryGetStringField(TEXT("type"), MessageType))
	{
		LogNetwork(FString::Printf(TEXT("Incoming JSON has no 'type' field: %s"), *InMessage));
		return;
	}

	if (MessageType == TEXT("pong"))
	{
		LogNetwork(TEXT("Received Pong"));
	}
	else if (MessageType == TEXT("error"))
	{
		LogNetwork(FString::Printf(TEXT("Received message: %s"), *InMessage));
		
		FString ErrorMessage;
		if (JsonObject->TryGetStringField(TEXT("message"), ErrorMessage))
		{
			LogNetwork(FString::Printf(TEXT("Server Error: %s"), *ErrorMessage));
			// OnSocketError.Broadcast(ErrorMessage);
		}
		else
		{
			LogNetwork(TEXT("Server Error: (no message field)"));
			// OnSocketError.Broadcast(TEXT("Unknown server error"));
		}
	}
	else
	{
		LogNetwork(FString::Printf(TEXT("Unknown message type received: %s"), *MessageType));
	}
}

void UWebSocketSystem::OnBinaryMessage_Native(const void* Data, SIZE_T Size, bool bIsLastFragment)
{
	LogNetwork(FString::Printf(TEXT("Received binary message (%d bytes) - Currently not supported"), Size));
	// 바이너리 메시지는 현재 사용하지 않음 (모든 오디오는 JSON의 Base64로 전송됨)
}

// --- Logging ---

void UWebSocketSystem::LogNetwork(const FString& Message)
{
	NETWORK_LOG(TEXT("[WS] %s"), *Message);
}
