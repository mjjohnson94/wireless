// // Create Chart.js configuration object, this acts as the top level structure for a Chart.js visualisation 

// const config = {
//     // Select chart type as line
//     type: 'line',
//     // Pass data object to the data argument, the object will be defined in the next step 
//     data: data,
// };

// // Create object named labels which will store each month of the year 
// // Chart.js provides utilities to assist in building visualisations 

// const labels = Utils.months({count: 7});

// // Create data object

// const data = {
//     labels: labels,
//     datasets: [{
//         label: 'My First Dataset',
//         data: [65, 59, 80, 81, 56, 55, 40],
//         fill: false,
//         borderColor: 'rgb(75, 192, 192)',
//         tension: 0.1
//       }]
// };

const ctx = document.getElementById('myChart');
      
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});