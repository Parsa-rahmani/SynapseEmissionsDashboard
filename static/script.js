fetch('/get_emissions')
    .then(response => response.json())
    .then(synapse_values => {
        let totalEmissions = 0;
        let emissionsHTML = '<h2>Monthly $SYN emissions on:</h2>';

        synapse_values.forEach(chain => {
            const monthlyValue = (chain.value * 30).toLocaleString(); // Convert to monthly value
            totalEmissions += chain.value * 30;
            emissionsHTML += `<p>${chain.network_name}: ${monthlyValue}</p>`;
        });

        document.getElementById('emissions').innerHTML = emissionsHTML;
        document.getElementById('total').innerHTML = `<h2>Total Monthly Emissions: ${totalEmissions.toLocaleString()}</h2>`;
    })
    .catch(error => console.error('An error occurred:', error));
