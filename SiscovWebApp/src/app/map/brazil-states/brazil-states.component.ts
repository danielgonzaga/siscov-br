import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';

import { ILocalsItem, LocalsListComponent } from 'src/app/shared/locals-list/locals-list.component';
import * as _ from 'lodash';
import { MapService } from '../services/map.service';

@Component({
  selector: 'app-brazil-states',
  templateUrl: './brazil-states.component.html',
  styleUrls: ['./brazil-states.component.css']
})
export class BrazilStatesComponent implements OnInit {
  @ViewChild(LocalsListComponent) localsListComponent: LocalsListComponent;

  states  = [];
  loading: boolean = false;
  isNewsModalOpen: boolean = false;
  variantStateId: number;

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
      // const normalizedStateName = state.nome.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
      try {
        (document.querySelector('#est_' + state.id) as HTMLElement).style.fill = state.color;
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
    let parsedStateId = +selectedStateId.split('_')[1];
    let selectedState = _.find(this.states, {id: parsedStateId});
    if(stateToBeUnselected === selectedState) {
      selectedState.isSelected = !selectedState.isSelected
      if(selectedState.isSelected) {
        (document.querySelector('#' + selectedStateId) as HTMLElement).style.fill = this.verifyColor(selectedState.color);
      } else {
        (document.querySelector('#' + selectedStateId) as HTMLElement).style.fill = selectedState.color;
      }
    } else {
      if(stateToBeUnselected) {
        stateToBeUnselected.isSelected = false;
        (document.querySelector('#est_' + stateToBeUnselected.id) as HTMLElement).style.fill = stateToBeUnselected.color;
      }
      (document.querySelector('#' + selectedStateId) as HTMLElement).style.fill = this.verifyColor(selectedState.color);
      selectedState.isSelected = true;
    }
    this.localsListComponent.goToScroll(parsedStateId);
  }

  onAccordionClick(id) {
    let stateToBeUnselected = _.find(this.states, {isSelected: true});
    let selectedState = _.find(this.states, {id: id});
    if(stateToBeUnselected === selectedState) {
      selectedState.isSelected = !selectedState.isSelected
      if(selectedState.isSelected) {
        (document.querySelector('#est_' + id) as HTMLElement).style.fill = this.verifyColor(selectedState.color);
      } else {
        (document.querySelector('#est_' + id) as HTMLElement).style.fill = selectedState.color;
      }
    } else {
      if(stateToBeUnselected !== undefined) {
        stateToBeUnselected.isSelected = false;
        (document.querySelector('#est_' + stateToBeUnselected.id) as HTMLElement).style.fill = stateToBeUnselected.color;
      }
      (document.querySelector('#est_' + id) as HTMLElement).style.fill = this.verifyColor(selectedState.color); 
      selectedState.isSelected = true;
    }
  }

  verifyColor(color) {
    if(color === '#0377fc')
      return '#025fca';
    else if(color === '#dce650')
      return '#b0b840';
    else if(color === '#cf4040')
      return '#a63333'
  }

  openNewsModal(event) {
    this.variantStateId = event;
    this.isNewsModalOpen = true;
  }

  closeNewsModal() {
    this.isNewsModalOpen = false;
  }

}
