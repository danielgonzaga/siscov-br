import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
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

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  ngOnChanges() {
    this.items.map(item => {
      item.id = item.nome.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_")
    })
  }

  goStatesMap() {
    this.router.navigateByUrl('/states');
  }

  goCountiesMap(stateId) {
    console.log("stateId: ", stateId);
    this.router.navigateByUrl('/states/' + stateId.toLowerCase());
  }

  verifyAccordionSelection(item) {
    this.onAccordionClick.emit(item.nome);
  }
}
