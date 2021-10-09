import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ILocalsItem } from 'src/app/shared/locals-list/locals-list.component';

@Injectable({
  providedIn: 'root'
})
export class MapService {

  private readonly API = 'http://localhost:5000/'

  constructor(private http: HttpClient) { }

  listAllRegions() {
    return this.http.get<any>(this.API + 'region');
  }
}
