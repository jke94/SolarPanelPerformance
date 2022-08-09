import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VerticalbarComponent } from './components/verticalbar/verticalbar.component';
import { NgChartsModule } from 'ng2-charts';
import { MainComponent } from './components/main/main.component';
import { DatesDatepickerComponent } from './components/dates-datepicker/dates-datepicker.component';
import { MatGridListModule} from '@angular/material/grid-list'
import { MatDatepickerModule} from '@angular/material/datepicker'
import { MatFormFieldModule} from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatNativeDateModule } from '@angular/material/core';
import { MatButtonModule } from '@angular/material/button';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DatesDatepickerService } from './services/dates-datepicker/dates-datepicker-service.service';
import { DataServiceService} from './services/data-service/data-service.service'
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    VerticalbarComponent,
    DatesDatepickerComponent,
    MainComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgChartsModule,
    MatGridListModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    HttpClientModule,
    MatButtonModule,
    MatInputModule,
    BrowserAnimationsModule,
    MatNativeDateModule,
  ],
  providers: [
    DatesDatepickerService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
