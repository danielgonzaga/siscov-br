import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MapService {

  private readonly API = 'http://localhost:5000/'

  constructor(private http: HttpClient) { }

  listAllRegions() {
    return this.http.get<any>(this.API + 'region');
  }

  listAllStates() {
    return this.http.get<any>(this.API + 'state');
  }

  listAllCounties(stateId) {
    return this.http.get<any>(this.API + 'state/' + stateId + '/county');
  }

  findStateByName(stateName) {
    return this.http.get<any>(this.API + 'state/' + stateName + '/id');
  }
}
