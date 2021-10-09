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
      (document.querySelector('#' + county.nome) as HTMLElement).style.fill = county.color;
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
