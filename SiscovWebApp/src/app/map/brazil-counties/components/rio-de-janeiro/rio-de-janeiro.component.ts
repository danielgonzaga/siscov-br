import { Component, OnInit } from '@angular/core';
import * as _ from 'lodash';
import { MapService } from '../../../services/map.service';


@Component({
  selector: 'app-rio-de-janeiro',
  templateUrl: './rio-de-janeiro.component.html',
  styleUrls: ['./rio-de-janeiro.component.css']
})
export class RioDeJaneiroComponent implements OnInit {

  counties = [];
  loading: boolean = false;
  stateName: string = 'Rio de Janeiro'

  constructor(private mapService: MapService) { }

  ngOnInit(): void {
    this.loading = true;
    this.mapService.findStateByName(this.stateName).subscribe(state => {

      this.mapService.listAllCounties(state.id).subscribe(county => {
        this.counties = county
        this.loading = false;
        this.colorizeLocals();
      })

    })
  }

  colorizeLocals() {
    this.counties.forEach(county => {
      const normalizedCountyName = county.nome.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
      try {
        (document.querySelector('#' + normalizedCountyName) as HTMLElement).style.fill = county.color;
      } catch {
        console.error("Local id not found.");
      }
    })
  }

  getLocal(event) {
    let regionToBeUnselected = _.find(this.counties, {isSelected: true});
    let selectedRegionId = event.target.attributes.id.nodeValue;
    let selectedRegion = _.find(this.counties, {id: selectedRegionId});
    if(regionToBeUnselected === selectedRegion) {
      selectedRegion.isSelected = !selectedRegion.isSelected
    } else {
      if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
      selectedRegion.isSelected = true;
    }
  }

  onAccordionClick(id) {
    let regionToBeUnselected = _.find(this.counties, {isSelected: true});
    const normalizedId = id.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
    let selectedRegion = _.find(this.counties, {id: normalizedId});
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
