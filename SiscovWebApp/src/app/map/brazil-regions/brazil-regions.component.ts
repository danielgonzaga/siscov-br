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
      const normalizedRegionName = region.nome.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
      try {  
        (document.querySelector('#' + normalizedRegionName) as HTMLElement).style.fill = region.color;
      } catch {
        console.error("Local id not found.");
      }
    })
  }

  getLocal(event) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    let selectedRegionId = event.target.attributes.id.nodeValue;
    let selectedRegion = _.find(this.regions, {id: selectedRegionId});
    if(regionToBeUnselected === selectedRegion) {
      selectedRegion.isSelected = !selectedRegion.isSelected
    } else {
      if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
      selectedRegion.isSelected = true;
    }
  }

  onAccordionClick(id) {
    let regionToBeUnselected = _.find(this.regions, {isSelected: true});
    const normalizedId = id.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
    let selectedRegion = _.find(this.regions, {id: normalizedId});
    if(regionToBeUnselected === selectedRegion) {
      selectedRegion.isSelected = !selectedRegion.isSelected
    } else {
      if(regionToBeUnselected !== undefined) {
        regionToBeUnselected.isSelected = false;
      } 
      selectedRegion.isSelected = true;
    }
  }
}
