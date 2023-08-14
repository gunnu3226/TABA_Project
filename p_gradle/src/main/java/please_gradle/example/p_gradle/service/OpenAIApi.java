package please_gradle.example.p_gradle.service;

import org.json.JSONArray;
import org.json.JSONObject;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class OpenAIApi {
    private static final String API_KEY = "api넣고써요";

    public  String ask(String prompt) {
        String reseponseBody = "";

        JSONObject jsonBody = new JSONObject();
        jsonBody.put("messages", new JSONArray()
                .put(new JSONObject()
                        .put("role", "system")
                        .put("content", "카드 이름 : 국민 청춘대로 톡톡카드 카드 혜택 : 스타벅스 60%할인/카드 이름 : 삼성카드 taptap O 카드 혜택 : 스타벅스 50%할인, 교통 10%할인, 통신 10% 할인 / 카드 이름 : LOCA LIKIT1.2 카드 혜택 : 국내외 모든 가맹점 1.2%할인 / 카드 이름 : 카드의 정석카트 혜택 : 조건없이 1%할인. 넌 앞에 카드 중 나에게 가장 좋은 혜택을 주는 카드를 추천해주는 채팅봇이야.1개만 추천해줘.카드이름과 혜택을 1줄로 요약해서 말해줘"))
                .put(new JSONObject()
                        .put("role", "user")
                        .put("content", prompt)));
        jsonBody.put("max_tokens",2000);
        jsonBody.put("temperature",0.0);
        jsonBody.put("model", "gpt-3.5-turbo");

        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("https://api.openai.com/v1/chat/completions"))
                    .header("Content-Type","application/json")
                    .header("Authorization", "Bearer " + API_KEY)
                    .POST(HttpRequest.BodyPublishers.ofString(jsonBody.toString()))
                    .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            reseponseBody = extractAnswer(response.body());
        } catch (Exception e) {
            e.printStackTrace();
        }

        return reseponseBody;
    }

    private String extractAnswer(String responseJson) {
        JSONObject jsonObject = new JSONObject(responseJson);

        if (jsonObject.has("choices")) {
            JSONObject messageObject = jsonObject.getJSONArray("choices")
                    .getJSONObject(0)
                    .getJSONObject("message");

            return messageObject.getString("content").trim();
        } else {
            System.err.println("Error in API response:" + responseJson);
            return "API 호출 중 오류가 발생했습니다.";
        }
    }
}
