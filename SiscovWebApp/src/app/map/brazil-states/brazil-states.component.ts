import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';
import * as _ from 'lodash';
import { MapService } from '../services/map.service';

@Component({
  selector: 'app-brazil-states',
  templateUrl: './brazil-states.component.html',
  styleUrls: ['./brazil-states.component.css']
})
export class BrazilStatesComponent implements OnInit {

  states  = [];
  loading: boolean = false;

  constructor(private router: Router, private mapService: MapService) { }

  ngOnInit(): void {
    this.loading = true;
    this.mapService.listAllStates().subscribe(state => {
      this.loading = false;
      this.states = state
      this.colorizeLocals();
    })
    
  }

  colorizeLocals() {
    this.states.forEach(state => {
      (document.querySelector('#' + state.nome) as HTMLElement).style.fill = state.color;
    })
  }

  goRegionsMap() {
    this.router.navigateByUrl('/regions');
  }

  getLocal(event) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    if(stateToBeUnselected) stateToBeUnselected.isSelected = false;
    let selectedStateId = event.target.attributes.id.nodeValue;
    let selectedState = _.find(this.states, {nome: selectedStateId});
    selectedState.isSelected = true;
  }

  onAccordionClick(id) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    if(stateToBeUnselected) stateToBeUnselected.isSelected = false;
    let selectedStateId = id;
    let selectedState = _.find(this.states, {nome: selectedStateId});
    selectedState.isSelected = !selectedState.isSelected;
  }

}
