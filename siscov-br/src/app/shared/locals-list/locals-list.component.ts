import { Component, Input, OnInit, ViewEncapsulation } from '@angular/core';

export interface ILocalsItem {
  name: string,
  isRegion: boolean,
  isState: boolean,
  isCounty: boolean,
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

  constructor() { }

  ngOnInit(): void {
  }

}
