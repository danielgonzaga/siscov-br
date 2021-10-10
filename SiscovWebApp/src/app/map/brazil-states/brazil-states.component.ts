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
      const normalizedStateName = state.nome.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
      try {
        (document.querySelector('#' + normalizedStateName) as HTMLElement).style.fill = state.color;
      } catch {
        console.error("Local id not found.");
      }
    })
  }

  goRegionsMap() {
    this.router.navigateByUrl('/regions');
  }

  getLocal(event) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    let selectedStateId = event.target.attributes.id.nodeValue;
    let selectedState = _.find(this.states, {id: selectedStateId});
    if(stateToBeUnselected === selectedState) {
      selectedState.isSelected = !selectedState.isSelected
    } else {
      if(stateToBeUnselected) stateToBeUnselected.isSelected = false;
      selectedState.isSelected = true;
    }
  }

  onAccordionClick(id) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    const normalizedId = id.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
    let selectedState = _.find(this.states, {id: normalizedId});
    if(stateToBeUnselected === selectedState) {
      selectedState.isSelected = !selectedState.isSelected
    } else {
      if(stateToBeUnselected !== undefined) {
        stateToBeUnselected.isSelected = false;
      } 
      selectedState.isSelected = true;
    }
  }

}
