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
import { NavbarComponent } from './components/navbar/navbar.component';

import { Routes, RouterModule } from '@angular/router';
import { ContactComponent } from './components/contact/contact.component';
import { WelcomePageComponent } from './components/welcome-page/welcome-page.component';

const rutas: Routes = [
  { path: '', component: WelcomePageComponent },
  { path: 'welcome-page', component: WelcomePageComponent },
  { path: 'data', component: MainComponent },
  { path: 'contact', component: ContactComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    VerticalbarComponent,
    DatesDatepickerComponent,
    MainComponent,
    NavbarComponent,
    WelcomePageComponent,
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
    RouterModule.forRoot(rutas)
  ],
  providers: [
    DatesDatepickerService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
