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


// const ctx = document.getElementById('myChart');
          
// new Chart(ctx, {
//   type: 'line',
//   data: {
//     labels: ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23'],
//     datasets: [{
//       label: 'Total Balance',
//       data: [1200, 1900, 1300, 1500, 1200, 1500],
//       borderWidth: 2,
//       borderColor: '#323ED1',
//       backgroundColor: '#323ED1',
//     }]
//   },

//   options: {
//       scales: {

//       x: {
//       grid: {
//       display: false}},

//       y: {
//       grid: {
//       display: false}}
    
//     }}})

{/* <script>
        
const NetBalance = document.getElementById('netBalance');

new Chart(NetBalance, {

  type: 'line',

      data: {
      labels: ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23'],
      datasets: [{
      label: 'Cumulative Balance',
      data: [12000, 19000, 16000, 15000, 17000, 20000],
      borderWidth: 1,
      borderColor: '#3E54AC',
      backgroundColor: '#3E54AC',
      }]
    },

    options: {
        scales: {

        x: {
        grid: {
        display: false}},

        y: {
        grid: {
        display: false}}
      
      }}})

</script> */}
