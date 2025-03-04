async function runPython() {
    let pyodide = await loadPyodide();
    await pyodide.loadPackage(["micropip"]);

    let response = await fetch("words_set.json");
    let wordsSet = new Set(await response.json());

    let text = document.getElementById("userInput").value;

    let pythonScript = `
import re

def words_check(text, words_set):
    text = text.lower()
    split_text = [re.sub(r"[^\\w'-]", "", word) for word in text.split()]
    split_text = [word for word in split_text if word]
    if not split_text:
        return 0.0
    existing_words = sum(1 for word in split_text if word in words_set)
    return existing_words / len(split_text)

words_set = ${JSON.stringify([...wordsSet])}
result = words_check('${text}', words_set)
result
    `;

    let result = await pyodide.runPythonAsync(pythonScript);
    document.getElementById("result").innerText = result.toFixed(2);
}
