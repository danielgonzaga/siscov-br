import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NavbarComponent } from './navbar/navbar.component';
import { SearchBarComponent } from './search-bar/search-bar.component';


@NgModule({
  declarations: [
    NavbarComponent,
    SearchBarComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    NavbarComponent,
    SearchBarComponent
  ]
})
export class SharedModule { }
