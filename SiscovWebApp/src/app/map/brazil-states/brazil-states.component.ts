import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';
import * as _ from 'lodash';

@Component({
  selector: 'app-brazil-states',
  templateUrl: './brazil-states.component.html',
  styleUrls: ['./brazil-states.component.css']
})
export class BrazilStatesComponent implements OnInit {

  states: ILocalsItem[] = [];
  // states: ILocalsItem[] = [
  //   {name: 'Acre', id: 'acre', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Alagoas', id: 'alagoas', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Amapá', id: 'amapa', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Amazonas', id: 'amazonas', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Bahia', id: 'bahia', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Ceará', id: 'ceara', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Distrito Federal', id: 'distrito_federal', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Espírito Santo', id: 'espirito_santo', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Goiás', id: 'goias', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Maranhão', id: 'maranhao', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Mato Grosso', id: 'mato_grosso', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Mato Grosso do Sul', id: 'mato_grosso_do_sul', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Minas Gerais', id: 'minas_gerais', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Pará', id: 'para', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Paraíba', id: 'paraiba', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Paraná', id: 'parana', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Pernambuco', id: 'pernambuco', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Piauí', id: 'piaui', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Rio de Janeiro', id: 'rio_de_janeiro', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Rio Grande do Norte', id: 'rio_grande_do_norte', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Rio Grande do Sul', id: 'rio_grande_do_sul', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Rondônia', id: 'rondonia', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Roraima', id: 'roraima', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Santa Catarina', id: 'santa_catarina', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'São Paulo', id: 'sao_paulo', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Sergipe', id: 'sergipe', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  //   {name: 'Tocantins', id: 'tocantins', isRegion: false, isState: true, isCounty: false, isSelected: false, variantCases: true, population: 50000000, totalCases: 1000000, totalDeaths: 200000},
  // ]

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  goRegionsMap() {
    this.router.navigateByUrl('/regions');
  }

  getLocal(event) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    if(stateToBeUnselected) stateToBeUnselected.isSelected = false;
    let selectedStateId = event.target.attributes.id.nodeValue;
    let selectedState = _.find(this.states, {id: selectedStateId});
    selectedState.isSelected = true;
  }

  onAccordionClick(id) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    if(stateToBeUnselected) stateToBeUnselected.isSelected = false;
    let selectedStateId = id;
    let selectedState = _.find(this.states, {id: selectedStateId});
    selectedState.isSelected = !selectedState.isSelected;
  }

}
