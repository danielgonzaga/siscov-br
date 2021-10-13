import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NavbarComponent } from './navbar/navbar.component';
import { LocalsListComponent } from './locals-list/locals-list.component';
import { AccordionModule } from 'primeng/accordion';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { LocalsListItemComponent } from './locals-list/components/locals-list-item/locals-list-item.component';
import { LoaderComponent } from './loader/loader.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { NewsModalComponent } from './news-modal/news-modal.component';
import { CarouselModule } from 'primeng/carousel';

@NgModule({
  declarations: [
    NavbarComponent,
    LocalsListComponent,
    LocalsListItemComponent,
    LoaderComponent,
    NotFoundComponent,
    NewsModalComponent,
  ],
  imports: [
    CommonModule,
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule,
    AccordionModule,
    CarouselModule,
  ],
  exports: [
    NavbarComponent,
    LocalsListComponent,
    LoaderComponent,
    NotFoundComponent,
    NewsModalComponent,
  ]
})

export class SharedModule { }
