import { Time } from "@angular/common"

export interface DailyProduction {
    Date:Date,
    MaxDailyProduction:number,
    DailyHistoricalAverage:number,
    MaxPoder:number,
    MaxPoderTime:Time,
}