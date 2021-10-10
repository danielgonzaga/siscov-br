import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlagoasComponent } from './alagoas.component';

describe('AlagoasComponent', () => {
  let component: AlagoasComponent;
  let fixture: ComponentFixture<AlagoasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlagoasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlagoasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
