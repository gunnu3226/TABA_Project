package please_gradle.example.p_gradle.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import please_gradle.example.p_gradle.service.GptService;

import java.util.HashMap;
import java.util.Map;

@RestController
@CrossOrigin
public class GptController {
    private final GptService gptService;

    @Autowired
    public GptController(GptService gptService) {
        this.gptService = gptService;
    }

    @PostMapping("/ask")
    public Map<String,String> ask(@RequestBody String prompt){
        Map<String,String> responseMap = new HashMap<>();
        String answer = gptService.ask(prompt);
        responseMap.put("answer", answer);
        return responseMap;
    }
}
