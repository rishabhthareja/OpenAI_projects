from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai_api_key = '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'

# Function to generate code based on the selected language and problem statement
def generate_code(language, problem_statement):
    openai.api_key = openai_api_key

    # Make the API call to the OpenAI model to generate code
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate {language} code for: {problem_statement}",
        temperature=0.7,
        max_tokens=4000
    )

    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        language = request.form['language']
        problem_statement = request.form['problem_statement']

        # Validate user input
        if not language or not problem_statement:
            error_msg = "Please fill in both language and problem statement fields."
            return render_template('index.html', output='', error_msg=error_msg)

        try:
            output = generate_code(language, problem_statement)
            return render_template('index.html', output=output, error_msg='')
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            return render_template('index.html', output='', error_msg=error_msg)

    return render_template('index.html', output='', error_msg='')

if __name__ == '__main__':
    app.run(debug=True)