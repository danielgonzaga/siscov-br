import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BrazilRegionsComponent } from './brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './brazil-states/brazil-states.component';
import { BrazilCountiesComponent } from './brazil-counties/brazil-counties.component';
import { SharedModule } from '../shared/shared.module';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule
  ],
  exports: [
    BrazilRegionsComponent,
    BrazilStatesComponent
  ]
})
export class MapModule { }
