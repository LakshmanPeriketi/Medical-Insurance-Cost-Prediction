async function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    // Get input values from UI
    const age = document.getElementById("age").value;
    const sex = document.getElementById("sex").value;
    const bmi = document.getElementById("bmi").value;
    const children = document.getElementById("children").value;
    const smoker = document.getElementById("smoker").value;
    const region = document.getElementById("region").value;
    const estPrice = document.getElementById("uiEstimatedPrice");
    const resultDiv = document.getElementById("result-container");

    // Use URLSearchParams for x-www-form-urlencoded data (matches Flask request.form)
    const formData = new URLSearchParams();
    formData.append('age', age);
    formData.append('sex', sex);
    formData.append('bmi', bmi);
    formData.append('children', children);
    formData.append('smoker', smoker);
    formData.append('region', region);

    const url = "http://127.0.0.1:5000/predict_insurance_charges";

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            estPrice.innerHTML = "$" + data.estimated_charges.toLocaleString();
            resultDiv.classList.remove("result-hidden"); // Show the result
        } else {
            alert("Error: Could not connect to the model server.");
        }
    } catch (error) {
        console.error("Request failed:", error);
        alert("Server is not running. Please start server.py first.");
    }
}