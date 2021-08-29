import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { SharedModule } from './shared/shared.module';
import { MapModule } from './map/map.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    SharedModule,
    MapModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
