import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { BrazilRegionsComponent } from './brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './brazil-states/brazil-states.component';
import { BrazilCountiesComponent } from './brazil-counties/brazil-counties.component';
import { SharedModule } from '../shared/shared.module';


@NgModule({
  declarations: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule,
    HttpClientModule
  ],
  exports: [
    BrazilRegionsComponent,
    BrazilStatesComponent
  ]
})
export class MapModule { }
