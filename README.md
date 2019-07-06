# A Flask app with Azure Cognitive Services

This simple web app uses Azure for text translation, text-to-speech conversion, and sentiment analysis of input text and translations. It's built with Python and Flask. The frontend is HTML with JavaScript. 
This project is based on a [Microsoft Azure Tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/tutorial-build-flask-app-translation-synthesis?toc=%2fazure%2fcognitive-services%2fspeech-service%2ftoc.json&bc=%2fazure%2fcognitive-services%2fspeech-service%2fbreadcrumb%2ftoc.json)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

    * Python 3.5.2 or later
    * Git tools
    * An IDE or text editor, such as Visual Studio Code or Atom
    * Chrome or Firefox
	
	You need the following items from your Azure account

    * A Translator Text subscription key
    * A Text Analytics subscription key
    * A Speech Services subscription key 

	* A config.py file on the root directory with the following structure
	
	```
	synthesize_key = "REPLACE_WITH_YOUR_KEY"
	sentiment_key = "REPLACE_WITH_YOUR_KEY"
	translate_key = "REPLACE_WITH_YOUR_KEY"
	region = "REPLACE_WITH_YOUR_REGION"
	```


### Installing

1. Clone this repository to your local machine
2. Create a virtual environment on the top directory

Windows
```
virtualenv venv
```
MacOs / Linux
```
virtualenv venv --python=python3
```

3. Activate the virtual environment

Windows - bash
```
source venv/Scripts/activate
```
Windows - Command Line
```
venv\Scripts\activate.bat
```

Windows - PowerShell
```
 venv\Scripts\Activate.ps1
```

MacOS / Linux
```
source venv/bin/activate
```
4. Install requests module ```pip install requests```

5. Install Flask ```pip install Flask```

6. Define the start file of the Flask app

In Windows
```
set FLASK_APP=app.py
```

MacOS / Linux
```
export FLASK_APP=app.py
```

7. Run the flask app ```flask run```

8. Check there are no error messages after running the command. Open a browser and go the URL provided (normally is http://127.0.0.1:5000/). You should now be able to see the single page app. Enter some text, select a language to translate, analyze and then convert to speech. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Supracortical

