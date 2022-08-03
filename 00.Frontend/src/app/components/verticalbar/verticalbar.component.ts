import { Component, OnInit } from '@angular/core';
import { ChartData } from 'chart.js';
import { ChartOptions } from 'chart.js';
import { DailyProduction } from 'src/app/models/interfaces/daily-production';
import { DataServiceService } from 'src/app/services/data-service/data-service.service';

@Component({
  selector: 'app-verticalbar',
  templateUrl: './verticalbar.component.html',
  styleUrls: ['./verticalbar.component.css']
})
export class VerticalbarComponent implements OnInit {

  data!: DailyProduction[];
  elements!: DailyProduction[];
  myValue!:Array<number>;

  salesData!: ChartData<'bar'>
  chartOptions: ChartOptions = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'April´s Production',
      },
    },
  };

  constructor(private dataServiceService: DataServiceService) {  }

  ngOnInit(): void {
    this.dataServiceService.getJSON().subscribe(data => {
      this.data = data as DailyProduction[];
      console.log(this.data)
      console.log(this.data.length)

    });

    var dateA = new Date("2022-04-01");
    var dateB = new Date("2022-05-01");

    this.dataServiceService.getJSON()
      .subscribe(data => {
        var tmp = data as DailyProduction[];

        this.elements = tmp.filter(function (item) {
          var itemTime = new Date(item.Date).getTime()
          return itemTime >= dateA.getTime() && itemTime <= dateB.getTime();
        })

        this.myValue = Array.from({length: this.elements.length}, (value, key) => key + 1)
        
        this.salesData = {
          labels: this.elements.map(i =>i.Date),
          datasets: [
            { label: 'Production (kWh)', data: this.elements.map(i =>i.MaxDailyProduction) }
          ],
        };
      });

  }
}
