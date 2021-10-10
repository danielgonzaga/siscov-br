import { Component, OnInit } from '@angular/core';

import * as _ from 'lodash';
import { MapService } from 'src/app/map/services/map.service';

@Component({
  selector: 'app-amapa',
  templateUrl: './amapa.component.html',
  styleUrls: ['./amapa.component.css']
})
export class AmapaComponent implements OnInit {

  counties = [];
  loading: boolean = false;
  stateName: string = 'Amapa'

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
      console.log("normalizedCountyName: ", normalizedCountyName);
      try {
        (document.querySelector('#' + normalizedCountyName) as HTMLElement).style.fill = county.color;
      } catch {
        console.error("Local id not found.");
      }
    })
  }

  getLocal(event) {
    let countyToBeUnselected = _.find(this.counties, {isSelected: true});
    let selectedCountyId = event.target.attributes.id.nodeValue;
    let selectedCounty = _.find(this.counties, {id: selectedCountyId});
    if(countyToBeUnselected === selectedCounty) {
      selectedCounty.isSelected = !selectedCounty.isSelected
    } else {
      if(countyToBeUnselected) countyToBeUnselected.isSelected = false;
      selectedCounty.isSelected = true;
    }
  }

  onAccordionClick(id) {
    let countyToBeUnselected = _.find(this.counties, {isSelected: true});
    const normalizedId = id.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,"_");
    let selectedCounty = _.find(this.counties, {id: normalizedId});
    if(countyToBeUnselected === selectedCounty) {
      selectedCounty.isSelected = !selectedCounty.isSelected
    } else {
      if(countyToBeUnselected !== undefined) {
        countyToBeUnselected.isSelected = false;
      } 
      selectedCounty.isSelected = true;
    }
  }

}
