import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

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