function clsbyid(id) {
    el = document.getElementById(id);
    el.style.display = "none";
}

function openbyid(id) {
    el = document.getElementById(id);
    el.style.display = "block";
}

function alternate(id) {
    el = document.getElementById(id);
    if (el.style.display == "block") {
        el.style.display = "none";
    }
    else {
        el.style.display = "block";
    }
}

function submitbyid(id) {
    f = document.getElementById(id);
    f.submit();
}

function load(chart, data) {
    chart.data.datasets[0].label = "Overused words";
    for (var i = 0; i < chart.data.labels.length + 1; i++) {
        chart.data.labels.pop();
    }
    for (var i = 0; i < chart.data.datasets[0].data.length + 1; i++) {
        chart.data.datasets[0].data.pop();
    }
    var labels = [];
    var values = [];
    for (var key in data) {
        labels.push(key);
        values.push(data[key]);
    }
    chart.data.labels = labels;
    chart.data.datasets[0].data = values;
    chart.reset();
    chart.update();
}

$(document).ready(function () {
    var myChart = $("#myChart")[0].getContext("2d");
    window.customChart = new Chart(myChart, {
        type: "bar",
        data: {
            labels: [],
            datasets: [{
                label: '',
                backgroundColor: 'beige',
                borderColor: 'orange',
                borderWidth: 3,
                data: []
            }],
            options: {
                animation: {
                    easing: 'easeInElastic',
                    duration: 2000,
                },
                responsive: true,
                maintainAspectRatio: false
            }
        }
    });
});