function enviarDatos() {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    const selection = document.querySelector('input[name="selection"]:checked');

    if (!file) {
        alert("Por favor, selecciona un archivo.");
        return;
    }

    if (!selection) {
        alert("Por favor, selecciona una técnica.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append("selection", selection.value);

    fetch("http://localhost:5001/csv", {
        method: "POST",
        body: formData,
    })
        .then((data) => {
            console.log("Bien")
        })
        // .then((data) => {
        //     window.location.href = "dashboard.html";
        // })
        .catch((error) => {
            console.error(error);
            alert("Hubo un error al subir el archivo. Por favor, inténtalo nuevamente.");
        });
}

function mostrarGraficas() {
    fetch("http://localhost:5001/graficas")
        .then((response) => {
            if (response.ok) {
                return response.json(); //Convertir a json
            } else {
                throw new Error("Error al obtener las gráficas");
            }
        })
        .then((data) => {
            const graphs = data.graphs;

            //Mostrar la Gráfica
            const graph = JSON.parse(graphs[0]);
            Plotly.newPlot("graph", graph.data, graph.layout);
        })
        .catch((error) => {
            console.error(error); // Manejar errores
            alert("Hubo un error al cargar la gráfica.");
        });
}