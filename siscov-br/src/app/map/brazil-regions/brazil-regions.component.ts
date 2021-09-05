import { Component, OnInit } from '@angular/core';

import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';
import * as _ from 'lodash';

@Component({
  selector: 'app-brazil-regions',
  templateUrl: './brazil-regions.component.html',
  styleUrls: ['./brazil-regions.component.css']
})
export class BrazilRegionsComponent implements OnInit {

  regions: ILocalsItem[] = [
    {name: 'Norte', id: 'norte', isRegion: true, isState: false, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Nordeste', id: 'nordeste', isRegion: true, isState: false, isCounty: false, isSelected: false, variantCases: false, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Centro-Oeste', id: 'centro_oeste', isRegion: true, isState: false, isCounty: false, isSelected: false, variantCases: false, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Sudeste', id: 'sudeste', isRegion: true, isState: false, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
    {name: 'Sul', id: 'sul', isRegion: true, isState: false, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  ]

  constructor() { }

  ngOnInit(): void {
  }

  getLocal(event) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
    let selectedRegionId = event.target.attributes.id.nodeValue;
    let selectedRegion = _.find(this.regions, {id: selectedRegionId});
    selectedRegion.isSelected = true;
  }

  onAccordionClick(id) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
    let selectedRegionId = id;
    let selectedRegion = _.find(this.regions, {id: selectedRegionId});
    selectedRegion.isSelected = !selectedRegion.isSelected;
  }
}
