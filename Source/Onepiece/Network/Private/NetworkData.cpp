// Copyright (c) 2025 Doppleddiggong. All rights reserved. Unauthorized copying, modification, or distribution of this file, via any medium is strictly prohibited. Proprietary and confidential.

/**
 * @file NetworkData.cpp
 * @brief FResponseHealth의 동작을 구현합니다.
 */
#include "NetworkData.h"

#include "JsonObjectConverter.h"
#include "NetworkLog.h"
#include "UCommonFunctionLibrary.h"
#include "Misc/Base64.h"
#include "Interfaces/IHttpResponse.h"
#include "Dom/JsonObject.h"
#include "Dom/JsonValue.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"
#include "Serialization/JsonWriter.h"

void FResponseHealth::SetFromHttpResponse(const TSharedPtr<IHttpResponse, ESPMode::ThreadSafe>& Response)
{
    if (Response.IsValid())
    {
        status = Response->GetResponseCode();
    }
}

void FResponseHealth::PrintData()
{
    FString OutputString;
    FJsonObjectConverter::UStructToJsonObjectString(
        *this,
        OutputString,
        0,
        0
    );
    NETWORK_LOG( TEXT("[RES] %s"), *OutputString);
}