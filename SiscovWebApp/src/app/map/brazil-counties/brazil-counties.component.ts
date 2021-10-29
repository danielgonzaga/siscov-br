import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { LocalsListComponent } from 'src/app/shared/locals-list/locals-list.component';
import { MapService } from '../services/map.service';
import * as _ from 'lodash';
import { takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-brazil-counties',
  templateUrl: './brazil-counties.component.html',
  styleUrls: ['./brazil-counties.component.css']
})
export class BrazilCountiesComponent implements OnInit {

  @ViewChild(LocalsListComponent) localsListComponent: LocalsListComponent;
  stateId = +this.route.snapshot.params.id;

  constructor(private route: ActivatedRoute, private mapService: MapService, private router: Router,) {
  }

  counties = [];
  loading: boolean = false;
  stateName: string = "";
  isNewsModalOpen: boolean = false;
  variantCountyId: number;
  private destroy$ = new Subject<boolean>();

  ngOnInit(): void {
    this.loading = true;
    setTimeout(() => {
      this.setStateName(this.stateId);
    }, 500);
    this.mapService.listAllCounties(this.stateId).pipe(
      takeUntil(this.destroy$)
    ).subscribe(county => {
      this.counties = county
      this.loading = false;
      this.colorizeLocals();
    })
  }

  ngOnDestroy() {
    this.destroy$.next(true);
  }

  setStateName(id) {
    switch(id) {
      case 11: 
        this.stateName = "Rondônia";
        break;
      case 12: 
        this.stateName = "Acre";
        break;
      case 13: 
        this.stateName = "Amazonas";
        break;
      case 14: 
        this.stateName = "Roraima";
        break;
      case 15: 
        this.stateName = "Pará";
        break;
      case 16: 
        this.stateName = "Amapá";
        break;
      case 17: 
        this.stateName = "Tocantins";
        break;
      case 21: 
        this.stateName = "Maranhão";
        break;
      case 22: 
        this.stateName = "Piauí";
        break;
      case 23: 
        this.stateName = "Ceará";
        break;
      case 24: 
        this.stateName = "Rio Grande do Norte";
        break;
      case 25: 
        this.stateName = "Paraíba";
        break;
      case 26: 
        this.stateName = "Pernambuco";
        break;
      case 27: 
        this.stateName = "Alagoas";
        break;
      case 28: 
        this.stateName = "Sergipe";
        break;
      case 29: 
        this.stateName = "Bahia";
        break;
      case 31: 
        this.stateName = "Minas Gerais";
        break;
      case 32: 
        this.stateName = "Espírito Santo";
        break;
      case 33: 
        this.stateName = "Rio de Janeiro";
        break;
      case 35: 
        this.stateName = "São Paulo";
        break;
      case 41: 
        this.stateName = "Paraná";
        break;
      case 42: 
        this.stateName = "Santa Catarina";
        break;
      case 43: 
        this.stateName = "Rio Grande do Sul";
        break;
      case 50: 
        this.stateName = "Mato Grosso do Sul";
        break;
      case 51: 
        this.stateName = "Mato Grosso"
        break;
      case 52: 
        this.stateName = "Goiás";
        break;
      default:
        this.router.navigateByUrl("/not-found");
    }
  }

  colorizeLocals() {
    this.counties.forEach(county => {
      try {
        (document.querySelector('#mun_' + county.id) as HTMLElement).style.fill = county.color;
      } catch {
        console.error("Local id #mun_" + county.id + " not found.");
      }
    })
  }

  getLocal(event) {
    let countyToBeUnselected = _.find(this.counties, {isSelected: true});
    let selectedCountyId = event.target.attributes.id.nodeValue;
    let parsedCountyId = +selectedCountyId.split('_')[1];
    let selectedCounty = _.find(this.counties, {id: parsedCountyId});
    if(countyToBeUnselected === selectedCounty) {
      selectedCounty.isSelected = !selectedCounty.isSelected;
      if(selectedCounty.isSelected) {
        (document.querySelector('#' + selectedCountyId) as HTMLElement).style.fill = this.verifyColor(selectedCounty.color);
      } else {
        (document.querySelector('#' + selectedCountyId) as HTMLElement).style.fill = selectedCounty.color;
      }
    } else {
      if(countyToBeUnselected) {
        countyToBeUnselected.isSelected = false;
        (document.querySelector('#mun_' + countyToBeUnselected.id) as HTMLElement).style.fill = countyToBeUnselected.color;
      }
      (document.querySelector('#' + selectedCountyId) as HTMLElement).style.fill = this.verifyColor(selectedCounty.color);
      selectedCounty.isSelected = true;
    }
    this.localsListComponent.goToScroll(parsedCountyId);
  }

  onAccordionClick(id) {
    let countyToBeUnselected = _.find(this.counties, {isSelected: true});
    let selectedCounty = _.find(this.counties, {id: id});
    if(countyToBeUnselected === selectedCounty) {
      selectedCounty.isSelected = !selectedCounty.isSelected
      if(selectedCounty.isSelected) {
        (document.querySelector('#mun_' + id) as HTMLElement).style.fill = this.verifyColor(selectedCounty.color);
      } else {
        (document.querySelector('#mun_' + id) as HTMLElement).style.fill = selectedCounty.color;
      }
    } else {
      if(countyToBeUnselected) {
        countyToBeUnselected.isSelected = false;
        (document.querySelector('#mun_' + countyToBeUnselected.id) as HTMLElement).style.fill = countyToBeUnselected.color;
      }
      (document.querySelector('#mun_' + id) as HTMLElement).style.fill = this.verifyColor(selectedCounty.color);
      selectedCounty.isSelected = true;
    }
  }

  verifyColor(color) {
    const colorLowerCase = color.toLowerCase();
    if(colorLowerCase === '#0377fc')
      return '#025fca';
      else if(colorLowerCase === '#f6c146')
      return '#c59a38';
    else if(colorLowerCase === '#cf4040')
      return '#a63333'
  }

  openNewsModal(event) {
    this.variantCountyId = event;
    this.isNewsModalOpen = true;
  }

  closeNewsModal() {
    this.isNewsModalOpen = false;
  }

}
