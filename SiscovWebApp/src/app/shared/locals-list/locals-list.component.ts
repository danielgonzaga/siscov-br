import { Component, ElementRef, EventEmitter, Input, OnInit, Output, QueryList, ViewChildren } from '@angular/core';

import * as _ from 'lodash';
import { LocalsListItemComponent } from './components/locals-list-item/locals-list-item.component';

export interface ILocalsItem {
  nome: string,
  id: string,
  isRegion: boolean,
  isState: boolean,
  isCounty: boolean,
  isSelected: boolean,
  variantCases: boolean,
  population: number,
  totalCases: number,
  totalDeaths: number,
  color: string,
}

@Component({
  selector: 'app-locals-list',
  templateUrl: './locals-list.component.html',
  styleUrls: ['./locals-list.component.css']
})
export class LocalsListComponent implements OnInit {

  @Input() items: ILocalsItem[] = [];
  @Output() onAccordionClick = new EventEmitter<string>();
  @Output() onClickOpenNewsModal = new EventEmitter();
  @ViewChildren(LocalsListItemComponent) viewChildren!: QueryList<LocalsListItemComponent>;
  
  constructor() { }

  ngOnInit(): void {
  }

  verifyAccordionSelection(item) {
    this.onAccordionClick.emit(item.id);
  }

  goToScroll(id) {
    let index = _.findIndex(this.items, function(item) { return item.id == id })
    this.viewChildren.toArray()[+index].scrollIntoView()
  }

  openNewsModal(event) {
    console.log("locals-list recebendo open. Event: ", event);
    this.onClickOpenNewsModal.emit(event);
  }
}
