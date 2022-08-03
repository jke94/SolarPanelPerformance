import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VerticalbarComponent } from './components/verticalbar/verticalbar.component';
import { NgChartsModule } from 'ng2-charts';
import { MainComponent } from './components/main/main.component';
import { MatGridListModule} from '@angular/material/grid-list'

import { DataServiceService} from './services/data-service/data-service.service'

import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    VerticalbarComponent,
    MainComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgChartsModule,
    MatGridListModule,
    HttpClientModule,
  ],
  providers: [

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
