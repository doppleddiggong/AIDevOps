// Copyright (c) 2025 Doppleddiggong. All rights reserved. Unauthorized copying, modification, or distribution of this file, via any medium is strictly prohibited. Proprietary and confidential.

/// @file NetworkData.h
/// @brief 네트워크 요청과 응답에 사용되는 구조체 및 설정을 정의합니다.
#pragma once

#include "CoreMinimal.h"
#include "UCustomNetworkSettings.h"
#include "Templates/SharedPointer.h"
#include "NetworkData.generated.h"

// =================================================================================
// Network Configuration
// 서버 주소와 포트를 설정합니다.
// =================================================================================
namespace NetworkConfig
{
    /// @brief 현재 서버 모드에 맞는 HTTP 엔드포인트 URL을 생성합니다.
    /// @param Endpoint [in] 호출할 상대 경로입니다.
    /// @return 모드와 포트가 적용된 전체 URL입니다.
    static FString GetFullUrl(const FString& Endpoint)
    {
        const EServerMode Mode = UCustomNetworkSettings::GetCurrentServerMode();
        const FServerConfig& Config = GetDefault<UCustomNetworkSettings>()->GetConfig(Mode);
        return Config.GetFullUrl(Endpoint);
    }

    /// @brief 현재 서버 모드에서 사용할 WebSocket 주소를 반환합니다.
    /// @return ws(s):// 형식의 소켓 접속 URL입니다.
    static FString GetSocketURL()
    {
        const EServerMode Mode = UCustomNetworkSettings::GetCurrentServerMode();
        const FServerConfig& Config = GetDefault<UCustomNetworkSettings>()->GetConfig(Mode);
        return Config.WebSocketUrl;
    }
}

namespace RequestAPI
{
    /// @brief 서버 상태 확인 엔드포인트입니다.
    static FString Health = FString("/health");
}


/// @brief 헬스 체크 응답을 전달하는 델리게이트입니다.
DECLARE_DELEGATE_TwoParams(FResponseHealthDelegate, FResponseHealth&, bool);
USTRUCT(BlueprintType)
struct FResponseHealth
{
    GENERATED_BODY()

    UPROPERTY(BlueprintReadWrite)
    int32 status = 0;

    /// @brief HTTP 응답을 파싱해 상태 정보를 갱신합니다.
    void SetFromHttpResponse(const TSharedPtr<class IHttpResponse, ESPMode::ThreadSafe>& Response);

    /// @brief 디버그 로그에 응답 내용을 출력합니다.
    void PrintData();
};