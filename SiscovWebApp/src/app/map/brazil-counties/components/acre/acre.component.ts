import { Component, OnInit } from '@angular/core';

import * as _ from 'lodash';
import { MapService } from '../../../services/map.service';

@Component({
  selector: 'app-acre',
  templateUrl: './acre.component.html',
  styleUrls: ['./acre.component.css']
})
export class AcreComponent implements OnInit {

  counties = [];
  loading: boolean = false;
  stateName: string = 'Acre'

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
      (document.querySelector('#' + normalizedCountyName) as HTMLElement).style.fill = county.color;
    })
  }

  getLocal(event) {
    let regionToBeUnselected = _.find(this.counties, {isSelected: true});
    if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
    let selectedRegionId = event.target.attributes.id.nodeValue;
    let selectedRegion = _.find(this.counties, {nome: selectedRegionId});
    selectedRegion.isSelected = true;
  }

  onAccordionClick(id) {
    let regionToBeUnselected = _.find(this.counties, {isSelected: true});
    if(regionToBeUnselected) regionToBeUnselected.isSelected = false;
    let selectedRegionId = id;
    let selectedRegion = _.find(this.counties, {nome: selectedRegionId});
    selectedRegion.isSelected = !selectedRegion.isSelected;
  }

}
