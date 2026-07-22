const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(express.static('/data/data/com.termux/files/home/ai_engine_site/public'));
app.use(express.json());

app.post('/api/build', async (req, res) => {
    const { prompt } = req.body;
    const outputPath = path.join(process.cwd(), 'generated_game.py');

    try {
        console.log("Requesting code from Ollama...");
        const response = await fetch('http://127.0.0.1:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'qwen2.5-coder:3b',
                prompt: `Write a complete Kivy mobile game based on this request: ${prompt}. Output ONLY raw Python code. No markdown.`,
                stream: false
            })
        });
        
        const data = await response.json();

        // CHECK: Does data or response exist?
        if (!data || !data.response) {
            console.error("AI Error: Received empty response from Ollama.", data);
            return res.status(500).json({ message: "AI failed to generate code. Check terminal logs." });
        }
        
        const gameCode = data.response.replace(/```python/g, '').replace(/```/g, '').trim(); 
        
        fs.writeFileSync(outputPath, gameCode);
        console.log(`Success: File written to ${outputPath}`);
        res.json({ message: "Game compiled successfully!" });

    } catch (err) {
        console.error("Server Error:", err);
        res.status(500).json({ message: "Server error: " + err.message });
    }
});

app.listen(3000, () => console.log('Factory running on http://localhost:3000'));
