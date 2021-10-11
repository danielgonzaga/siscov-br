import { Component, ElementRef, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';

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

  constructor(private router: Router, private el: ElementRef<HTMLElement>) { }

  ngOnInit(): void {
    // setTimeout(() => {
    //   const element = document.querySelector('#mun_1200708'); // id of the scroll to element
    //   element.scrollIntoView();
    // }, 5000)
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

  goCountiesMap(stateId) {
    this.router.navigateByUrl('/states/' + stateId);
  }

  verifyAccordionSelection(item) {
    this.onAccordionClick.emit(item.id);
  }
}
