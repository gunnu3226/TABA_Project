package please_gradle.example.p_gradle.service;

import org.springframework.stereotype.Service;

@Service
public class GptService {
    private final  OpenAIApi openAIApi;

    public  GptService(){
        this.openAIApi = new OpenAIApi();
    }

    public String ask(String prompt) {
        try {
            return openAIApi.ask(prompt);
        } catch (Exception e) {
            e.printStackTrace();
            return "API 호출 중 오류가 발생했습니다: " + e.getMessage();
        }
    }
}
