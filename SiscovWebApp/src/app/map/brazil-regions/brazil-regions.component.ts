import { Component, OnInit } from '@angular/core';

import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';
import * as _ from 'lodash';
import { MapService } from '../services/map.service';

@Component({
  selector: 'app-brazil-regions',
  templateUrl: './brazil-regions.component.html',
  styleUrls: ['./brazil-regions.component.css']
})
export class BrazilRegionsComponent implements OnInit {

  regions = [];
  loading: boolean = false;

  constructor(private mapService: MapService) { }

  ngOnInit(): void {
    this.loading = true;
    this.mapService.listAllRegions().subscribe(region => {
      this.regions = region
      this.loading = false;
      this.colorizeLocals();
    })
    
  }

  colorizeLocals() {
    this.regions.forEach(region => {
      try {  
        (document.querySelector('#' + region.nome) as HTMLElement).style.fill = region.color;
      } catch {
        console.error("Local id not found.");
      }
      region['id']=region['nome'];
    })
  }

  getLocal(event) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    let selectedRegionId = event.target.attributes.id.nodeValue;
    let selectedRegion = _.find(this.regions, {nome: selectedRegionId});
    if(regionToBeUnselected === selectedRegion) {
      selectedRegion.isSelected = !selectedRegion.isSelected
      if(selectedRegion.isSelected) {
        (document.querySelector('#' + selectedRegionId) as HTMLElement).style.fill = this.verifyColor(selectedRegion.color);
      } else {
        (document.querySelector('#' + selectedRegionId) as HTMLElement).style.fill = selectedRegion.color;
      }
    } else {
      if(regionToBeUnselected) {
        regionToBeUnselected.isSelected = false;
        (document.querySelector('#' + regionToBeUnselected.id) as HTMLElement).style.fill = regionToBeUnselected.color;
      }
      (document.querySelector('#' + selectedRegionId) as HTMLElement).style.fill = this.verifyColor(selectedRegion.color);
      selectedRegion.isSelected = true;
    }
  }

  onAccordionClick(id) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    let selectedRegion = _.find(this.regions, {id: id});
    if(regionToBeUnselected === selectedRegion) {
      selectedRegion.isSelected = !selectedRegion.isSelected
      if(selectedRegion.isSelected) {
        (document.querySelector('#' + id) as HTMLElement).style.fill = this.verifyColor(selectedRegion.color);
      } else {
        (document.querySelector('#' + id) as HTMLElement).style.fill = selectedRegion.color;
      }
    } else {
      if(regionToBeUnselected !== undefined) {
        regionToBeUnselected.isSelected = false;
        (document.querySelector('#' + regionToBeUnselected.id) as HTMLElement).style.fill = regionToBeUnselected.color;
      }
      (document.querySelector('#' + id) as HTMLElement).style.fill = this.verifyColor(selectedRegion.color); 
      selectedRegion.isSelected = true;
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
}
