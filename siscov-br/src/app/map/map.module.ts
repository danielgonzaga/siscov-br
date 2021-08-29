import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrazilRegionsComponent } from './brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './brazil-states/brazil-states.component';



@NgModule({
  declarations: [
    BrazilRegionsComponent,
    BrazilStatesComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    BrazilRegionsComponent,
    BrazilStatesComponent
  ]
})
export class MapModule { }
