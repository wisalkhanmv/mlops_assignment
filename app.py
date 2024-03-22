from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the pre-trained model and scaler
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Convert the input data into a numpy array
    input_data = [[data['alcohol'], data['malic_acid'], data['ash'], data['alcalinity_of_ash'], data['magnesium'],
                   data['total_phenols'], data['flavanoids'], data['nonflavanoid_phenols'], data['proanthocyanins'],
                   data['color_intensity'], data['hue'], data['od280/od315_of_diluted_wines'], data['proline']]]

    # Scale the input data using the loaded scaler
    input_data_scaled = scaler.transform(input_data)

    # Make predictions using the loaded model
    prediction = model.predict(input_data_scaled)

    # Convert the prediction into a human-readable label
    if prediction == 0:
        label = 'Class 0'
    elif prediction == 1:
        label = 'Class 1'
    else:
        label = 'Class 2'

    # Prepare the response
    response = {
        'prediction': label
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
