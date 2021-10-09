import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BrazilCountiesComponent } from './map/brazil-counties/brazil-counties.component';

import { BrazilRegionsComponent } from './map/brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './map/brazil-states/brazil-states.component';

const routes: Routes = [
    {
        path: '',
        component: BrazilRegionsComponent,
    },
  {
    path: 'regions',
    component: BrazilRegionsComponent,
  },
  {
    path: 'states',
    component: BrazilStatesComponent,
  },
  {
    path: 'states/:name',
    component: BrazilCountiesComponent,
  }
];

@NgModule({

  imports: [
      RouterModule.forRoot(routes)
  ],
  
  exports: [
      RouterModule
  ],
})
export class AppRoutingModule { }