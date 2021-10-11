import { Component, Input, OnInit, QueryList, ViewChildren } from '@angular/core';

import * as _ from 'lodash';
import { ScrollableItemDirective } from 'src/app/directives/scrollable-item.directive';
import { MapService } from '../../../services/map.service';

@Component({
  selector: 'app-acre',
  templateUrl: './acre.component.html',
  styleUrls: ['./acre.component.css']
})
export class AcreComponent implements OnInit {

  @Input() stateId: number;
  counties = [];
  loading: boolean = false;

  constructor(private mapService: MapService) { }
  @ViewChildren(ScrollableItemDirective) scrollableItems: QueryList<ScrollableItemDirective>

  ngOnInit(): void {
    this.counties = [{"color":"#0377fc","id":1200013,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Acrel\u00e2ndia","population":15721,"totalCases":1427,"totalDeaths":21,"variantCases":false},{"color":"#0377fc","id":1200054,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Assis Brasil","population":7649,"totalCases":1092,"totalDeaths":15,"variantCases":false},{"color":"#0377fc","id":1200104,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Brasil\u00e9ia","population":27123,"totalCases":1828,"totalDeaths":36,"variantCases":false},{"color":"#0377fc","id":1200138,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Bujari","population":10572,"totalCases":126,"totalDeaths":7,"variantCases":false},{"color":"#0377fc","id":1200179,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Capixaba","population":12280,"totalCases":439,"totalDeaths":3,"variantCases":false},{"color":"#0377fc","id":1200203,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Cruzeiro do Sul","population":89760,"totalCases":10686,"totalDeaths":183,"variantCases":false},{"color":"#0377fc","id":1200252,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Epitaciol\u00e2ndia","population":18979,"totalCases":4276,"totalDeaths":22,"variantCases":false},{"color":"#0377fc","id":1200302,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Feij\u00f3","population":34986,"totalCases":2028,"totalDeaths":31,"variantCases":false},{"color":"#0377fc","id":1200328,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Jord\u00e3o","population":8628,"totalCases":18,"totalDeaths":1,"variantCases":false},{"color":"#0377fc","id":1200336,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"M\u00e2ncio Lima","population":19643,"totalCases":925,"totalDeaths":26,"variantCases":false},{"color":"#0377fc","id":1200344,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Manoel Urbano","population":9701,"totalCases":93,"totalDeaths":3,"variantCases":false},{"color":"#0377fc","id":1200351,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Marechal Thaumaturgo","population":19727,"totalCases":1659,"totalDeaths":12,"variantCases":false},{"color":"#0377fc","id":1200385,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Pl\u00e1cido de Castro","population":20147,"totalCases":406,"totalDeaths":12,"variantCases":false},{"color":"#0377fc","id":1200807,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Porto Acre","population":19141,"totalCases":183,"totalDeaths":13,"variantCases":false},{"color":"#0377fc","id":1200393,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Porto Walter","population":12497,"totalCases":267,"totalDeaths":4,"variantCases":false},{"color":"#0377fc","id":1200401,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Rio Branco","population":419452,"totalCases":18495,"totalDeaths":885,"variantCases":false},{"color":"#0377fc","id":1200427,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Rodrigues Alves","population":19767,"totalCases":71,"totalDeaths":11,"variantCases":false},{"color":"#0377fc","id":1200435,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Santa Rosa do Purus","population":6893,"totalCases":142,"totalDeaths":4,"variantCases":false},{"color":"#0377fc","id":1200500,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Sena Madureira","population":47168,"totalCases":2147,"totalDeaths":105,"variantCases":false},{"color":"#0377fc","id":1200450,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Senador Guiomard","population":23446,"totalCases":319,"totalDeaths":12,"variantCases":false},{"color":"#0377fc","id":1200609,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Tarauac\u00e1","population":43730,"totalCases":7007,"totalDeaths":60,"variantCases":false},{"color":"#0377fc","id":1200708,"isCounty":true,"isRegion":false,"isSelected":false,"isState":false,"nome":"Xapuri","population":19866,"totalCases":353,"totalDeaths":13,"variantCases":false}]
    this.colorizeLocals();
    // this.loading = true;
    // this.mapService.listAllCounties(this.stateId).subscribe(county => {
    //   this.counties = county
    //   this.loading = false;
    //   this.colorizeLocals();
    // })
  }

  colorizeLocals() {
    this.counties.forEach(county => {
      try {
        (document.querySelector('#mun_' + county.id) as HTMLElement).style.fill = county.color;
      } catch {
        console.error("Local id not found.");
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
    if(color === '#0377fc')
      return '#025fca';
    else if(color === '#dce650')
      return '#b0b840';
    else if(color === '#cf4040')
      return '#a63333'
  }

}
