import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';

export interface ILocalsItem {
  name: string,
  id: string,
  isRegion: boolean,
  isState: boolean,
  isCounty: boolean,
  isSelected: boolean,
  variantCases: boolean,
  population: number,
  totalCases: number,
  totalDeaths: number,
}

@Component({
  selector: 'app-locals-list',
  templateUrl: './locals-list.component.html',
  styleUrls: ['./locals-list.component.css']
})
export class LocalsListComponent implements OnInit {

  @Input() items: ILocalsItem;
  @Output() onAccordionClick = new EventEmitter<string>();

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

  verifyAccordionSelection(item) {
    this.onAccordionClick.emit(item.id);
  }
}
