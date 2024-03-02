# explain2me

This project is a Chrome extension named "explain2me" that allows users to scrape a web page for text and use a Language
Model (LLM) to summarize the page in 250 words. The extension consists of both a client-side component and a server-side component.

## Usage

*1.* Clone the repository - change in to directory of your choice and run:

```sh
git clone https://github.com/tkmamidi/explain2me.git
```

*2.* Navigate to the project directory

```sh
cd EXPLAIN2ME/server
```

*3.* Setup OpenAI API key

Please signup and create new api key in [openAI platform](https://platform.openai.com/api-keys). Create a `.env` file
and add/update `OPENAI_API_KEY="<your-api-key>"` in the file.

*4.* Install required packages and run the app

```sh
# Install packages
pip install requirements.txt

# Run the app
uvicorn main:app
```

*5.* Add the chrome extension

To use the "explain2me" Chrome extension, simply go to Chrome Extensions tab and turn on the developer mode (top right
toggle button). Click on "Load unpacked" and navigate to the extension directory of the repo and select it. Once
installed, you can click on the extension icon on any webpage to open the popup window. From there, the extension will
scrape the page for text and provide a summary using the Language Model (LLM).

## Contributing

If you would like to contribute to this project, please follow the guidelines in the CONTRIBUTING.md file.
