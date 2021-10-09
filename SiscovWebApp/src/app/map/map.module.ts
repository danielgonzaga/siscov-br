import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { BrazilRegionsComponent } from './brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './brazil-states/brazil-states.component';
import { SharedModule } from '../shared/shared.module';
import { RioDeJaneiroComponent } from './brazil-counties/components/rio-de-janeiro/rio-de-janeiro.component';
import { AcreComponent } from './brazil-counties/components/acre/acre.component';
import { BrazilCountiesComponent } from './brazil-counties/brazil-counties.component';


@NgModule({
  declarations: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent,
    AcreComponent,
    RioDeJaneiroComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule,
    HttpClientModule,
  ],
  exports: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent,
    AcreComponent,
    RioDeJaneiroComponent,
  ]
})
export class MapModule { }
