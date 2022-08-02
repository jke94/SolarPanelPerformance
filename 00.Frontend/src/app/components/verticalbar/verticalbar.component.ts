import { Component, OnInit } from '@angular/core';
import { ChartData } from 'chart.js';
import { ChartOptions } from 'chart.js';

@Component({
  selector: 'app-verticalbar',
  templateUrl: './verticalbar.component.html',
  styleUrls: ['./verticalbar.component.css']
})
export class VerticalbarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  salesData: ChartData<'bar'> = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [
      { label: 'Mobiles', data: [1000, 1200, 1050, 2000, 500] },
      { label: 'Laptop', data: [200, 100, 400, 50, 90] },
      { label: 'AC', data: [500, 400, 350, 450, 650] },
      { label: 'Headset', data: [1200, 1500, 1020, 1600, 900] },
    ],
  };
  chartOptions: ChartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Monthly Sales Data',
      },
    },
  };
}
