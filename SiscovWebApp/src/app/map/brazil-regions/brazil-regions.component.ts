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

  constructor(private mapService: MapService) { }

  ngOnInit(): void {
    this.mapService.listAllRegions().subscribe(region => {
      // this.regions.length = 0;
      this.regions = region
      this.colorizeLocals();
    })
    
  }

  colorizeLocals() {
    this.regions.forEach(region => {
      (document.querySelector('#' + region.nome) as HTMLElement).style.fill = region.color;
    })
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
